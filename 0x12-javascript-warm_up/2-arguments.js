#!/usr/bin/node
argv = require('process').argv;
argLen = argv.length

if (argv[2] === undefined)
	console.log('No argument');
else if (argLen == 3)
	console.log('Argument found');
else
	console.log('Arguments found');
