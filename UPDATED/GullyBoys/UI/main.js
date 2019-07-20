const {app, BrowserWindow} = require('electron');
const path = require('path');
const url = require('url');

let win;

function CreateWindow(){
    win = new BrowserWindow({width:1920, height:1080, icon:__dirname+'/icon.png'});
    
    win.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file:',
        slashes: true
    }));
    

    console.log("WINDOWS CREATED");
    
    // DEVELOPER TOOLS KE LIYE
    win.webContents.openDevTools(); 
    
    win.on('closed',() => {
        win=null;
    });
}
app.on('ready', CreateWindow);

app.on('window-all-closed',() => {
    if(process.platform !== 'darwin'){
        app.quit();
    }
});
