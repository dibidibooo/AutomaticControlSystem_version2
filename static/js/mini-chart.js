var charts_info = null

var oldest_datetime = null

// function for get all info from API
function getInfo(url, success_function)
{
    console.log(">>> getInfo", url)

    // get info from api
    fetch(url).then(response => {
        // get from json
        response.json().then(info => {
            charts_info = info.data
            console.log(">>> success get info", charts_info);
            success_function(charts_info)
        })
        return response.json();
    }).then(function(data) {
        console.log(data);
    }).catch(function(e) {
        console.error("Error", e);
    });
}

// start function
getInfo("/api/get_results1", createAllCharts)


// create all charts on data from API
function createAllCharts(charts_info){
    console.log(">> createAllCharts", charts_info);

    var resetCssClasses = function(e) {
        var t = document.querySelectorAll("button");
        Array.prototype.forEach.call(t, function(e) {
            e.classList.remove("active")
        }), e.target.classList.add("active")
    };

    charts_info.forEach(component => {
        console.log(">> component", component);

        const component_index = component.object_index;
        component.values.forEach(value => {
            // min chart
            const mini_chart_el_id = `mini-chart-${component_index}-${value.name}`
            const mini_options = createChartObject(value.values.slice(-10)) // !change slice for good range info
            const mini_chart = new ApexCharts(document.getElementById(mini_chart_el_id), mini_options)
            mini_chart.render();
        })

        // Full chart
        component.date_values.forEach(value => {
            console.log(">v", value)
            // full chart
            const full_chart_el_id = `full-chart-${component_index}-${value.name}`
            const full_options = createFullChartObject(value.values, value.values[0][0], value.values[value.values.length - 1][0])
            const full_chart = new ApexCharts(document.getElementById(full_chart_el_id), full_options)
            full_chart.render();

            setDateButtons(full_chart_el_id, full_chart, value.values[0][0], value.values[value.values.length - 1][0])
        })

    })
}


function setDateButtons(chart_name, chart, start_date, end_date){
    console.log(">>> setDateButtons", chart_name, `six_months-${chart_name}`)
    var resetCssClasses = function(e) {
        var t = document.querySelectorAll("button");
        Array.prototype.forEach.call(t, function(e) {
            e.classList.remove("active")
        }), e.target.classList.add("active")
    };

    const one_month = document.getElementById(`one_month-${chart_name}`)
    console.log(">>one_month 1", new Date(end_date))
    if(one_month){
        one_month.addEventListener("click", e => {
        console.log(">>one_month ")
            resetCssClasses(e), chart.updateOptions({
                xaxis: {
                    min: new Date(end_date).setMonth(new Date(end_date).getMonth() - 1),
                    max: end_date
                }
            })
        })
    }


    const six_months = document.getElementById(`six_months-${chart_name}`)
    console.log(">! six_months", six_months)
    if(six_months){
        six_months.addEventListener("click", e => {
        console.log(">>six_months ")
            resetCssClasses(e), chart.updateOptions({
                xaxis: {
                    min: new Date(end_date).setMonth(new Date(end_date).getMonth() - 6),
                    max: end_date
                }
            })
        })
    }

    const one_year = document.getElementById(`one_year-${chart_name}`)
    if(one_year){
        one_year.addEventListener("click", e => {
        console.log(">>one_year ")
            resetCssClasses(e), chart.updateOptions({
                xaxis: {
                    min: new Date(end_date).setFullYear(new Date(end_date).getFullYear() - 1),
                    max: end_date
                }
            })
        })
    }

    const all_b = document.getElementById(`all-${chart_name}`)
    if(all_b){
        all_b.addEventListener("click", e => {
            console.log(">>all_b ")
            resetCssClasses(e), chart.updateOptions({
                xaxis: {
                    min: start_date,
                    max: end_date
                }
            })
        });
    }
}


function createChartObject(data){
    return{
    series: [{
        name: "",
        data: data
    }],
    chart: {
        type: "area",
        height: 50,
        sparkline: {
            enabled: !0
        }
    },
    stroke: {
        curve: "smooth",
        width: 2
    },
    colors: ["#3452e1"],
    fill: {
        type: "gradient",
        gradient: {
            shadeIntensity: 1,
            inverseColors: !1,
            opacityFrom: .45,
            opacityTo: .05,
            stops: [25, 100, 100, 100]
        }
    },
    tooltip: {
        fixed: {
            enabled: !1
        },
        x: {
            show: !1
        },
        marker: {
            show: !1
        }
    }
};
}


function createFullChartObject(data, start_date, end_date){
    console.log("> full chart", data, start_date, end_date)
    console.log("> full chart", data, Date(start_date), Date(end_date))
    return {
    series: [{
        name: "Компонент",
        data: data
    }],
    chart: {
        type: "area",
        height: 240,
        toolbar: "false"
    },
    dataLabels: {
        enabled: !1
    },
    stroke: {
        curve: "smooth",
        width: 2
    },
    markers: {
        size: 0,
        style: "hollow"
    },
    xaxis: {
        type: "datetime",
        min: start_date,
        max: new Date(),
        tickAmount: 6
    },
    tooltip: {
        x: {
            format: "dd MMM yyyy"
        }
    },
    colors: ["#f1b44c"],
    fill: {
        type: "gradient",
        gradient: {
            shadeIntensity: 1,
            opacityFrom: .6,
            opacityTo: .05,
            stops: [42, 100, 100, 100]
        }
    }
};
}