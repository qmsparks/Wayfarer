// $addPost = $('{{post.title}}')
const $button = $('#add_post')
const test = function() {
    console.log("Working")
}
$button.on("click", test)

const $button2 = $(".button")
console.log("workqa")
$button2.on("click", test)

const $delete = $('#delete')
console.log($delete)

const remove = function() {
    const $popup = $(`<h1 id = popup> Are you sure?</h1>`)
    const $yes = $('<input class="btn btn-outline-dark deletebutton" type="submit" value="Yes">')
    const $no = $('<button id = no> No </button>')
    const $form = $('#form')
    $form.append($popup)
    $form.append($yes)
    $form.append($no)

}

$delete.on("click", remove)

$editButton = $(".btn btn-light btn-sm")

const message = function() {
    window.alert("Wrong Profile")
}

$editButton.on("click", message)