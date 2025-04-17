
/*JavaScript code for handling Socket.IO and user interactions*/
// Connect to the Socket.IO server, you should use here your ipv4 adress
var url = "http://localhost:9000";

const socket = io.connect(url);
// Event handler for the 'connect' event
socket.on('connect', () => {
    // Request screen data when connected
    socket.emit('requestScreen_continious');
});

const screenImage = document.getElementById('screenImage');
const loader = document.getElementById("loader")
const autofocusInput = document.getElementById('autofocusInput');

normal_keyboard = true;
scroll = "OFF";

let DraggingEnded = true;
let isDragging = false;

// Event handler for receiving screen data interactively
socket.on('screenData_interactive', (data) => {
    // Update the screen image with the received data
    screenImage.src = `data:image/png;base64,${data.image}`;
    loader.style.display = "none";
});

// Event handler for receiving screen data continuisly (1.5s)
socket.on('screenData_continious', (data) => {
    screenImage.src = `data:image/png;base64,${data.image}`;
    loader.style.display = "none";
});

