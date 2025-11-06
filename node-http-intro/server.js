const http = require('http');              // Imports the built in HTTP module, letting you create servers, handle requests, and send responses.

const server = http.createServer((req, res) => {       // Creates an instance of HTTP
    // Req and res are parameters for the callback function, req (client request), res (server response)

    console.log('Method:', req.method, 'URL:', JSON.stringify(req.url));


  // res.writeHead prepares the reponse to take Staus and Headers
  // Status code 200 = Success
  // 'Content-Type': 'text/plain' Tells the browser you're sending plain text not HTML, JSON etc


  // Ends the reponse and sends the message to the client
 if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Welcome to the Home Page!');
 } else if (req.url === '/about') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('This is the About Page.');

 } else if (req.url === '/contact') {
    // Example demonstrating how to use JSON which is just a different way to send text to the browser
    // JSON is structured data with keys and values that machines can parse, text is just raw characters
    res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ message: 'You’ve reached the Contact Page.' }));
 } else if (req.url === '/time') {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  // respond is JSON string {time: date(in international standard time format)}
  res.end(JSON.stringify({ time: new Date().toISOString() })); 
 } else if (req.url.startsWith('/headers')) {
  // Return all request headers as JSON
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify(req.headers, null, 2)); 
 } else {
  res.writeHead(404, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ error: '404 - Page Not Found' }));
}
});




server.listen(3000, () => {                                   // Tells the server to listen on port 3000 and execute a function logging this message
  console.log('Server running at http://localhost:3000/');    // When this link is opened Node executes the callback function
});
