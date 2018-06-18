/* ---------------------------------------------------------------------
 Pop Up form
 ---------------------------------------------------------------------= */

jQuery.noConflict();
jQuery(document).ready(function(){
jQuery('.close').click(function(){
  jQuery('#popup-container').fadeOut();
  jQuery('#active-popup').fadeOut();
});
var visits = Cookies.get('visits') || 0;
visits++;

Cookies.set('visits', visits, { expires: 1, path: '/' });

console.debug(Cookies.get('visits'));

if ( Cookies.get('visits') > 1 ) {
jQuery('#active-popup').hide();
jQuery('#popup-container').hide();
} else {
  var pageHeight = jQuery(document).height();
  jQuery('<div id="active-popup"></div>').insertBefore('body');
  jQuery('#active-popup').css("height", pageHeight);
  jQuery('#popup-container').show();
}

if (Cookies.get('noShowWelcome')) { jQuery('#popup-container').hide(); jQuery('#active-popup').hide(); }
});

jQuery(document).mouseup(function(e){
var container = jQuery('#popup-container');

if( !container.is(e.target)&& container.has(e.target).length === 0)
{
container.fadeOut();
jQuery('#active-popup').fadeOut();
}

});
