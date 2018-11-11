FUNCTION_MODULE = 'index.js'
FUNCTION_ENTRYPOINT = 'helloHttp'

function loadUserFunction(module, entrypoint) {
    const userFunction = require(`./${module}`)[entrypoint];
    return userFunction
}

// Load the user's function
const userFunction = loadUserFunction(FUNCTION_MODULE, FUNCTION_ENTRYPOINT);

// Create an Express app
const express = require('express');
const app = express();
const bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

// Invoke the user's function on any request
app.all('*', userFunction);

const host = '0.0.0.0'
const port = '8000'
const server = app.listen(port, () => {
    console.log(`Listening at http://${host}:${port}`);
});