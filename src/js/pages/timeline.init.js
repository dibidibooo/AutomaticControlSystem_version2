$('#timeline-carousel').owlCarousel({
    items: 1,
    loop: false,
    margin:0,
    nav: true,
    navText : ["<i class='mdi mdi-chevron-left'></i>","<i class='mdi mdi-chevron-right'></i>"],
    dots: false,
    responsive:{
        576:{
            items:2
        },

        768:{
            items:4
        },
    }
});