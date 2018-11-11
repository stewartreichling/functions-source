/**
 * A starter HTTP function.
 * 
 * Get started by editing the code in the `helloHttp` function. This
 * function is based on the Express framework <http://https://expressjs.com/>.
 */

/**
 * A function that responds to an HTTP request.
 *
 * @param {Object} req Cloud Function request context.
 *                     More info: https://expressjs.com/en/api.html#req
 * @param {Object} res Cloud Function response context.
 *                     More info: https://expressjs.com/en/api.html#res
 */
exports.helloHttp = (req, res) => {
    res.send(`Hello ${req.body.name || 'World'}!`);
};