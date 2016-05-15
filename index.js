'use strict';

const electron = require('electron');
const url = require("url");
const http = require("http");
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

let mainWindow;

function createWindow () {
  // Create the browser window.
  mainWindow = new BrowserWindow({show:false});

  // KASUMI TECHNOPARK SAKURA
  var kasumi = 'http://www.kasumi.co.jp/tenpo/kennan/technopark_sakura.html';
  
  mainWindow.loadURL(kasumi);
  mainWindow.webContents.on("did-finish-load", function(){
    mainWindow.webContents.savePage("./data/weia.html", "HTMLComplete", function(error){
      if(!error){
        console.log("save complete");
        mainWindow.close();
      }else{
        console.log("ERROR! NO SAVE")
      }
    })
  })
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
app.on('ready', createWindow);

// Quit when all windows are closed.
app.on('window-all-closed', function () {
  // On OS X it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

