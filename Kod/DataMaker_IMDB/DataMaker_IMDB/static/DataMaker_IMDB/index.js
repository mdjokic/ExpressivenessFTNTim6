$('.multi-field-wrapper').each(function() {
    var $wrapper = $('.multi-fields', this);
    var i = 1;

    $(".add-field", $(this)).click(function(e) {
        $('.multi-field:first-child', $wrapper).clone(true).appendTo($wrapper).find('input').attr('name', 'personField' + i++).val('').focus();
    });

    $('.multi-field .remove-field', $wrapper).click(function() {
        if ($('.multi-field', $wrapper).length > 1)
            $(this).parent('.multi-field').remove();
    });
});