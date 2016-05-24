'use strict';

const electron = require('electron');
const url = require("url");
const http = require("http");
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

let kasumiWindow;

function createWindow () {
    // KASUMI TECHNOPARK SAKURA
    var kasumi = 'http://www.kasumi.co.jp/tenpo/kennan/technopark_sakura.html';
    var kasumiWindow = new BrowserWindow({show:false});

    // AEON TSUKUBA STATION
    var aeon = 'http://shop.aeon.jp/store/01/0117270/';
    var aeonWindow = new BrowserWindow({show:false});

    kasumiWindow.loadURL(kasumi);
    kasumiWindow.webContents.on("did-finish-load", function(){
        kasumiWindow.webContents.savePage("./data/kasumi_sakura.html", "HTMLComplete", function(error){
            if(!error){
                console.log("save complete");
            }else{
                console.log("ERROR! NO SAVE");
            }

            aeonWindow.loadURL(aeon);
            aeonWindow.webContents.on("did-finish-load", function(){
                aeonWindow.webContents.savePage("./data/aeon.html", "HTMLComplete", function(error){
                    if(!error){
                        console.log("save complete");
                    }else{
                        console.log("ERROR! NO SAVE");
                    }
                    app.quit();

                })


            })
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

