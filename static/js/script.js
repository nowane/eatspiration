$(document).ready(function () {
	$('.sidenav').sidenav({
		edge: "right"
	});
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
                                <a class="remove-list-item">
                                    <span class="sr-only">Remove Ingredient</span>
                                    <i class="fas fa-trash-alt"></i>
                                </a>
                            </li>`;
	$(this).parent().before(ingredientListItem);
});

// Remove ingredient list item when thrash icon is clicked
$('#ingredients').on("click", ".remove-list-item", function (event) {
	$(this).parent().remove();
});

// Add preperation item to list when plus icon is clicked
$('#prep_step .add-prep-list-item').click(function (event) {
	let prepStep = `<li class="collection-item">
                        <div class="input-field">
                            <textarea name="prep_step" class="materialize-textarea" required></textarea>
                            <label for="prep_step">Step Description</label>
                        </div>
						<a class="remove-list-item">
							<i class="fas fa-trash-alt"></i>
							<span class="sr-only">Remove Preperation Step</span>
						</a>
                    </li>`;
	$(this).parent().before(prepStep);
});

// Remove preperation list item when thrash icon is clicked
$('#prep_step').on("click", ".remove-list-item", function (event) {
	$(this).parent().remove();
});