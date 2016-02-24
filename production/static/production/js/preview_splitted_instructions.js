jQuery(function ($) {
    var $instructions_fields = $(':input[name^="cutting_instructions"]')
    $instructions_fields.on('keyup', function () {
        var instructions = [];
        $instructions_fields.each(function (index, item) {
            instructions.push($(item).val())
        });
        var instructions_text = instructions.join('___'); // 'A:47.8  I:30.25->A:31 I:30.25(1)___I:16.25->A:31.8 I:20.2(1)'
        $.getJSON(
            cutting_instruction_format_url,
            {'instructions': instructions_text},
            function (data) {
                $('.cutting-patterns-preview').html(data.formatted_instructions)
            }
        );
    })
    $instructions_fields.trigger('keyup')
});