// set the dimensions and margins of the graph
var margin = {top: 20, right: 20, bottom: 30, left: 40},
    width = 860 - margin.left - margin.right,
    height = 250 - margin.top - margin.bottom;

// set the ranges
var x = d3.scale.ordinal()
      .rangeRoundBands([0, width],0.1);
var y = d3.scale.linear()
      .range([height, 0]);

var xAxis = d3.svg.axis()
      .scale(x)
      .orient("bottom");
  
var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left")
      .ticks(10);
      
// append the svg object to the body of the page
// append a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg1 = d3.select("#bar_chart").append("svg").classed("barChart",true)
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");

var div2= d3.select("body").append("div")
    .attr("class", "tooltip")         
    .style("opacity", 0);
var bcolor=d3.scale.ordinal()
      .range(["#ffec17", "#ffdd00","#ffc300","#ffaa00","#ff9500","#ff7b00"]);
// get the data
d3.csv("datasets/victims_byAge.csv", function(error, data) {
if (error) throw error;

// format the data
data.forEach(function(d) {
  d.value = +d.value;
});

// Scale the range of the data in the domains
x.domain(data.map(function(d) { return d.category; }));
y.domain([0, d3.max(data, function(d) { return d.total_victims; })]);


  svg1.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
    .selectAll("text")
      .style("text-anchor", "end")
      .attr("dx", "-1em")
      .attr("dy", "-.15em")
      .attr("transform", "rotate(-30)" );

  svg1.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end");

  svg1.selectAll("bar")
      .data(data)
    .enter().append("rect")
      .each(function(d,i){
            d3.select(this).attr({
                  fill:bcolor.range()[i],
            })
      })
      .attr("x", function(d) { return x(d.category); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.total_victims); })
      .attr("height", function(d) { return height - y(d.total_victims); })
      .on("mouseover",function(d){
            div2.transition()
                  .duration(200)
                  .style("opacity",.9);
            div2.html("Victims total : "+ d.total_victims)
                  .style("left",(d3.event.pageX +10)+"px")
                  .style("top",(d3.event.pageY -50)+"px");
      })
      .on("mouseout",function(d){
            div2.transition()
                  .duration(500)
                  .style("opacity",0);
      });

});