$(document).ready(function () {
	$('.sidenav').sidenav({
		edge: "right"
	});
	$('select').formSelect();

	// Tim Nelson's validation function from the task manager project
	validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});

// Check if confirm password matches password and set valid/invalid
$("#password-confirm").keyup(function () {
	if ($(this).val() === $("#password").val()) {
		$(this).removeClass("invalid").addClass("valid");
		this.setCustomValidity("");
	} else {
		$(this).removeClass("valid").addClass("invalid");
		this.setCustomValidity("No match");
	}
});

// Based on this example
// https://stackoverflow.com/questions/53400879/how-to-add-new-item-to-materialize-css-collection
// Add ingredient item to list when plus icon is clicked
$('#ingredients .add-ingredient-list-item').click(function (event) {
	let ingredientListItem = `<li class="collection-item">
                                <div class="input-field">
                                    <input name="ingredients" type="text" maxlength="70" required>
                                    <label for="ingredients">Ingredient</label>
                                </div>
                                <a class="remove-ingredient-list-item">
                                    <span class="sr-only">Remove Ingredient</span>
                                    <i class="fas fa-trash-alt"></i>
                                </a>
                            </li>`;
	$(this).parent().before(ingredientListItem);
});

// Remove ingredient list item when thrash icon is clicked
$('#ingredients').on("click", ".remove-ingredient-list-item", function (event) {
	$(this).parent().remove();
});

// Add preparation item to list when plus icon is clicked
$('#prep_steps .add-prep-list-item').click(function (event) {
    let prepListItem = `<li class="collection-item">
                            <div class="input-field">
                                <input name="prep_steps" type="text" maxlength="140" required>
                                <label for="prep_steps">Preparation Step</label>
                            </div>
                            <a class="remove-prep-list-item">
                                <span class="sr-only">Remove Preparation Step</span>
                                <i class="fas fa-trash-alt"></i>
                            </a>
                        </li>`;
            $(this).parent().before(prepListItem);
});

// Remove preparation list item when thrash icon is clicked
$('#prep_steps').on("click", ".remove-prep-list-item", function (event) {
	$(this).parent().remove();
});