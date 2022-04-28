
var charts_info = null

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
    charts_info.forEach(component => {
        console.log(">> component", component);
        const component_index = component.object_index;
        component.values.forEach(value => {
            // min chart
            const mini_chart_el_id = `mini-chart-${component_index}-${value.name}`
            const mini_options = createChartObject(value.values.slice(-10)) // !change slice for good range info
            const mini_chart = new ApexCharts(document.getElementById(mini_chart_el_id), mini_options)
            mini_chart.render();

            // full chart
            const full_chart_el_id = `full-chart-${component_index}-${value.name}`
            const full_options = createChartObject(value.values)
            const full_chart = new ApexCharts(document.getElementById(full_chart_el_id), full_options)
            full_chart.render();
        })
    })
}

function createChartObject(data){
    return{
    series: [{
        name: "",
        data: data
    }],
    chart: {
        type: "area",
        height: 40,
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
