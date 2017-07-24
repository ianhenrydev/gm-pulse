var express = require('express');
var router = express.Router();
var PythonShell = require('python-shell');

/* GET users listing. */
router.get('/', function(req, res, next) {
    var options = {
        args: ['this is a test quote'],
    };
    PythonShell.run('classifier.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
        res.send(results);
    });
});

module.exports = router;
