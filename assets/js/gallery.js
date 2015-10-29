
$(document).ready(function() {
  $('#product-page-image').magnificPopup({type:'image'});
});

$('#product-page-image-container').magnificPopup({
  delegate: 'a',
  type: 'image',
  gallery:{
    enabled:true,
    preload: [0,2], // read about this option in next Lazy-loading section

    navigateByImgClick: true,
  
    arrowMarkup: '<button title="%title%" type="button" class="mfp-arrow mfp-arrow-%dir%"></button>', // markup of an arrow button
  
    tPrev: 'Previous (Left arrow key)', // title for left button
    tNext: 'Next (Right arrow key)', // title for right button
    tCounter: '<span class="mfp-counter">%curr% of %total%</span>' // markup of counter
  }
});