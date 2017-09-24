var data; // a global
var width = window.innerWidth - 100;
var height = window.innerHeight - 100;
var radius = width / 50;
var diameter = 2 * radius;
var counter = 0;
var tip = d3.tip()
    .attr('class', 'd3-tip')
    .offset([-10, 0])
    .html(function(d) {
        var strName = "<strong>Name:</strong> <span style='color:red'>" + d.name + "</span></br></br>";
        var strHEX = "<strong>Hex value:</strong> <span style='color:red'>" + d.hex + "</span></br></br>";
        var strRGB = "<strong>RGB value:</strong> <span style='color:red'>" + d.rgb + "</span></br></br>";
        return strName + strHEX + strRGB;
    })
var svg = d3.select(document.body)
    .append('svg')
    .attr('width', width)
    .attr('height', height)
    .call(tip);
var circles;
d3.json("./crayola.json", function(error, json) {
    if (error) return console.warn(error);
    data = json;
    visualizeit();
});
window.addEventListener('resize', function() {
    width = window.innerWidth - 100;
    height = window.innerHeight - 100;
    radius = width / 50;
    diameter = 2 * radius;
    counter = 0;
    svg
        .attr('width', width)
        .attr('height', height)
    refreshit();
})
var visualizeit = function() {
    circles = svg
        .selectAll('colors')
        .data(data)
        .enter()
        .append('circle')
        .attr('class', 'colors')
        .attr('cx', function(el, index) {
            return radius + (index * diameter) % width;
        })
        .attr('cy', function(el, index) {
            if ((index * diameter) % width === 0)
                counter++;
            return (counter) * (diameter + radius);
        })
        .attr('r', radius)
        .attr('fill', function(el, index) {
            return el.hex;
        })
        .on('mouseover', tip.show)
        .on('mouseout', tip.hide)
}
var refreshit = function() {
    circles
        .attr('cx', function(el, index) {
            return radius + (index * diameter) % width;
        })
        .attr('cy', function(el, index) {
            if ((index * diameter) % width === 0)
                counter++;
            return (counter) * (diameter + radius);
        })
        .attr('r', radius)
        .attr('fill', function(el, index) {
            return el.hex;
        })
}