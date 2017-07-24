var express = require('express');
var router = express.Router();
var PythonShell = require('python-shell');

/* GET users listing. */
router.get('/:quote?', function(req, res, next) {
    var options = {};
    if (req.params.quote) {
        options = {
            args: [req.params.quote],
        };
    }
    PythonShell.run('classifier.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        console.log('results: %j', results);
        res.json(results);
    });
});

module.exports = router;
