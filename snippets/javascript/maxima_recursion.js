var i = 0;
 
function recurse () {
    i++;
    recurse();
}
 
try {
    recurse();
} catch (ex) {
    alert('i = ' + i + '\nerror: ' + ex);
}
