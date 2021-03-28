var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'bar',

    // The data for our dataset
    data: {
        labels: labels,
        datasets: [{
            label: 'Количество участников',
            backgroundColor: 'rgb(255, 187, 0)',
            borderColor: 'rgb(255, 99, 132)',
            data: [45, 10, 5]
        }]
    },

    // Configuration options go here
    options: {}
});