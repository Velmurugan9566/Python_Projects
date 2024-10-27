use('velu');

// Run a find command to view items sold on April 4th, 2014.
const salesOnApril4th = db.getCollection('stu').find();

// Print a message to the output window.
console.log(`${salesOnApril4th} sales occurred in 2014.`);
