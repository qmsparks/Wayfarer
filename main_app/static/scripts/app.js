// $addPost = $('{{post.title}}')
const $button = $('#add_post')
const test = function(){
    console.log("Working")
}
$button.on("click", test)

const $button2 = $(".button")
console.log("workqa")
$button2.on("click", test)

const $delete = $('#delete')
console.log($delete)

const remove = function(){
    const $popup = $(`<h1 id = popup> Are you sure?</h1>`)
    const $yes = $('<button id = yes> Yes </button>')
    const $no = $('<button id = no> No </button>')
    const $div = $('#delete_div')
    $div.append($popup)
    $div.append($yes)
    $div.append($no)

}

$delete.on("click", remove)