#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const destination = process.argv[4];

if (fileA && fileB && destination) {
  try {
    const dataA = fs.readFileSync(fileA, 'utf8');
    const dataB = fs.readFileSync(fileB, 'utf8');
    fs.writeFileSync(destination, dataA + dataB, 'utf8');
  } catch (error) {
    console.error(error);
  }
} else {
  console.error('Usage: ./103-concat.js <fileA> <fileB> <destination>');
}
