jQuery(function ($) {
    var $select_recipe_tbody = $('.select-recipe tbody');

    // Apply filter to fetch results and display it
    $('.recipe-filter-form')
        .on('reset', function () { // Clean currently filled body
            $select_recipe_tbody.empty();
        })
        .on('change', function () {
            var $form = $(this);
            $.post($form.attr('action'), $form.serialize(), function (data) {
                $select_recipe_tbody.empty();
                if (data.recipe_list.length == 0) {
                    $select_recipe_tbody.append(
                        '<tr>' +
                        '<td colspan="7">' +
                        '<div class="alert alert-warning"><i class="glyphicon glyphicon-info-sign"></i> No recipes found</td>' +
                        '</td>' +
                        '</tr>'
                    )
                } else {
                    $.each(data.recipe_list, function (index, recipe) {
                        $select_recipe_tbody.append(
                            '<tr data-id="' + recipe.id + '">' +
                            '<td>' + recipe.retail_size + '</td>' +
                            '<td>' + recipe.coating + '</td>' +
                            '<td>' + recipe.panel_depth + '</td>' +
                            '<td>' + recipe.cradle_depth + '</td>' +
                            '<td>' + recipe.cradle_width + '</td>' +
                            '<td>' + recipe.spray_color + '</td>' +
                            '<td><i class="glyphicon glyphicon-' + ((recipe.is_active) ? 'check' : 'unchecked') + '"></i></td>' +
                            '</tr>'
                        )
                    })
                }
            })
        });

    function recipe_row_to_text($tr) {
        var values = [];
        $tr.find('td').each(function () {
            var text = $(this).text();
            if (text != 'None') {
                values.push(text)
            }
        });
        // Slice it to not use is active field
        return values.slice(0,-1).join('--')
    }

    $('#modal-recipes-chooser')
        .on('show.bs.modal', function (e) { // Save popup trigger
          $(this).data()['bs.modal'].options.source = $(e.relatedTarget).data('source');
        })
        .on('click', 'tr[data-id]', function () {  // Make rows selectable and select recipe field
            var $selected_recipe = $(this);
            var $modal = $selected_recipe.parents('.modal');
            var text = $selected_recipe.text()
            $($modal.data()['bs.modal'].options.source)
                .val($selected_recipe.data('id')) // Set field value
                .closest('.form-group') // find the node which hold the text
                .find('.recipe-text')
                .text(recipe_row_to_text($selected_recipe));  // Set text
            $modal.modal('toggle')
        });
});
