const socket = io();

let actions = [];
let currentBatch = [];
let drawing = false;

function setup() {
    createCanvas(windowWidth, windowHeight);
    background(232);

    socket.emit("request-init");
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
    redrawAll();
}

function mousePressed() {
    drawing = true;
}

function mouseReleased() {
    drawing = false;
    sendBatch();
}

function draw() {
    if (drawing && mouseIsPressed) {
        let action = createLine(pmouseX, pmouseY, mouseX, mouseY);
        applyAction(action);
        actions.push(action);
        currentBatch.push(action);
    }
}

function createLine(x1, y1, x2, y2) {
    return {
        type: "line",
        args: [x1, y1, x2, y2],
        color: "#000000",
        weight: 2
    };
}

function applyAction(action) {
    stroke(action.color);
    strokeWeight(action.weight);

    switch (action.type) {
        case "line":
            line(...action.args);
            break;
    }
}

function redrawAll() {
    background(232);
    for (let action of actions) {
        applyAction(action);
    }
}

function sendBatch() {
    if (currentBatch.length > 0) {
        socket.emit("whiteboard-update", currentBatch);
        currentBatch = [];
    }
}

socket.on("whiteboard-update", (data) => {
    for (let action of data) {
        applyAction(action);
        actions.push(action);
    }
});

socket.on("init", (data) => {
    actions = data;
    redrawAll();
});
