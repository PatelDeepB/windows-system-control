import win32gui
import win32ui
import win32con
import win32api
import win32com.client
from PIL import Image
import io
import requests
import time
import argparse
from screeninfo import get_monitors

def get_screen_size():
    for m in get_monitors():
        # Get the dimensions of the screen
        width = m.width
        height = m.height
        return width, height

def main(host, key):
    r = requests.post(host+'/new_session', json={'_key': key})
    if r.status_code != 200:    
        print('Server not available.')
        return

    shell = win32com.client.Dispatch('WScript.Shell')
    PREV_IMG = None
    i = 0
    while True:
        width, height = get_screen_size()

        # device context
        hdesktop = win32gui.GetDesktopWindow()
        desktop_dc = win32gui.GetWindowDC(hdesktop)
        img_dc = win32ui.CreateDCFromHandle(desktop_dc)

        # memory context
        mem_dc = img_dc.CreateCompatibleDC()

        screenshot = win32ui.CreateBitmap()
        screenshot.CreateCompatibleBitmap(img_dc, width, height)
        mem_dc.SelectObject(screenshot)

        bmpinfo = screenshot.GetInfo()

        # copy into memory 
        mem_dc.BitBlt((0, 0), (width, height), img_dc, (0, 0), win32con.SRCCOPY)

        bmpstr = screenshot.GetBitmapBits(True)

        pillow_img = Image.frombytes('RGB',
                                      (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
                                      bmpstr, 'raw', 'BGRX')

        if i == 0:
            pillow_img.save('ss.png')  # Save the screenshot as ss.png
            i = 1

        with io.BytesIO() as image_data:
            pillow_img.save(image_data, 'PNG')
            image_data_content = image_data.getvalue()

        if image_data_content != PREV_IMG:
            files = {}
            filename = str(round(time.time() * 1000)) + '_' + key
            files[filename] = ('img.png', image_data_content, 'multipart/form-data')

            try:
                r = requests.post(host+'/capture_post', files=files)
            except Exception as e:
                pass

            PREV_IMG = image_data_content
        else:
            # print('no desktop change')
            pass

        # events
        try:
            r = requests.post(host+'/events_get', json={'_key': key})
            data = r.json()
            for e in data['events']:
                print(e)
                x, y = win32api.GetCursorPos()
                print("Mouse position: X =", x, "Y =", y)

                # if e['type'] == 'click':
                #     win32api.SetCursorPos((e['x'], e['y']))
                #     time.sleep(0.1)
                #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, e['x'], e['y'], 0, 0)
                #     time.sleep(0.02)
                #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, e['x'], e['y'], 0, 0)
                ################
                # if e['type'] == 'click':
                #     # Adjust the coordinates to match the remote screen size
                #     remote_width, remote_height = get_screen_size()
                #     remote_x = int(e['x'] * remote_width / width)
                #     remote_y = int(e['y'] * remote_height / height)
                #     win32api.SetCursorPos((remote_x, remote_y))
                #     time.sleep(0.1)
                #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, remote_x, remote_y, 0, 0)
                #     time.sleep(0.02)
                #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, remote_x, remote_y, 0, 0)

                if e['type'] == 'click':
                    current_width, current_height = get_screen_size()
                    current_x = int(e['x'] * current_width / width)
                    current_y = int(e['y'] * current_height / height)
                    original_x, original_y = win32api.GetCursorPos()
                    win32api.SetCursorPos((current_x, current_y))
                    time.sleep(0.1)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, current_x, current_y, 0, 0)
                    time.sleep(0.02)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, current_x, current_y, 0, 0)
                    win32api.SetCursorPos((original_x, original_y))


                if e['type'] == 'keydown':
                    cmd = ''

                    if e['shiftKey']:
                        cmd += '+'

                    if e['ctrlKey']:
                        cmd += '^'

                    if e['altKey']:
                        cmd += '%'

                    if len(e['key']) == 1:
                        cmd += e['key'].lower()
                    else:
                        cmd += '{'+e['key'].upper()+'}'

                    print(cmd)
                    shell.SendKeys(cmd)

        except Exception as err:
            print(err)
            pass

        # free
        mem_dc.DeleteDC()
        win32gui.DeleteObject(screenshot.GetHandle())
        time.sleep(0.2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='pyRD')
    parser.add_argument('addr', help='server address', type=str)
    parser.add_argument('key', help='access key', type=str)
    args = parser.parse_args()

    main(args.addr, args.key)
