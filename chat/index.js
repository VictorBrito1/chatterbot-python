var app = require('express')();
var http = require('http');
var server = http.Server(app)
var io = require('socket.io')(server);
var port = process.env.PORT || 3000;
var botURL = 'http://127.0.0.1:5000/'

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
});

getRespostaDoBot = (msg) => {
  const url = botURL + "answer/" + msg
  http.get(url, (response) => {
    let data = '';
    response.on('data', (chunk) => {
      data += chunk;
    });

    response.on('end', () => {
      io.emit('chat message', data)
    });

  }).on("error", (err) => {
    console.log("Error: " + err.message);
  });
}

io.on('connection', function (socket) {
  socket.on('chat message', function (msg) {
    io.emit('chat message', msg);
    getRespostaDoBot(msg)
  });
});

server.listen(port, function () {
  console.log('listening on *:' + port);
});
