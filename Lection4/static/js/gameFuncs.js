const player = document.getElementById('player');
const playerFieldTop = document.getElementById('playerField').style.top.match(/(\d+)/);
const playerFieldLeft = document.getElementById('playerField').style.left.match(/(\d+)/);
const playerFieldHeight = document.getElementById('playerField').style.height.match(/(\d+)/);
const playerFieldWidth = document.getElementById('playerField').style.width.match(/(\d+)/);

player.style.position = 'absolute';

document.addEventListener("DOMContentLoaded", fillPlayerField())

function curentPosition(side) {
    if (side == "top") {
        playerCoord = player.style.top.match(/(\d+)/);
    } else if (side == "left") {
        playerCoord = player.style.left.match(/(\d+)/);
    }
    return parseInt(playerCoord[0]);
}

function moveDown() {
    if (curentPosition("top") + 170 < playerFieldHeight[0]) {
        player.style.top = curentPosition("top") + 170 + 'px';
    }
}

function moveUp() {
    if (curentPosition("top") > parseInt(playerFieldTop[0])) {
        player.style.top = curentPosition("top") - 170 + 'px';
    }
}

function moveLeft() {
    if (curentPosition("left") > parseInt(playerFieldLeft[0])) {
        player.style.left = curentPosition("left") - 170 + 'px';
    }
}

function moveRight() {
    if (curentPosition("left") + 170 < playerFieldWidth[0]) {
        player.style.left = curentPosition("left") + 170 + 'px';
    }
}

function fillPlayerField() {
    const playerField = document.querySelector('#playerField');

    for (let positionTop = 70; positionTop < playerFieldHeight[0]; positionTop += 170) {
        for (let positionLeft = 70; positionLeft < playerFieldWidth[0]; positionLeft += 170) {
            let fieldDot = document.createElement('div');

            fieldDot.setAttribute('style', 'width: 30px; height: 30px; background-color: red; border-radius: 100%; position: absolute; top: ' + positionTop + 'px; left: ' + positionLeft + 'px; z-index: -100;');

            playerField.appendChild(fieldDot);

            console.log(positionTop + ', ' + positionLeft)
        }
    }
}