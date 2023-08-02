// Show-Hide new link panel
function btn_new_bookmark(){
    var form_new_link = document.getElementById("form_new_link");
    if (form_new_link.style.display === "none"){
        form_new_link.style.display = "block";
    } 
    else{
        form_new_link.style.display = "none";
    }
}


// Close edit panel
function span_close(id){
    modal_edit.style.display = "none";
}


// If user click the window, close the modal
window.onclick = function(event){
    var modals = document.getElementsByClassName("modal")
    for(modal of modals){
        if(event.target == modal){
            modal.style.display = 'none';
        }
    }
}


// On mouse over show the buttons
function show_buttons(id){
    // console.log("show_buttons");
    btn_edit = document.getElementById("btn_edit_" + id);
    btn_delete = document.getElementById("btn_delete_" + id);
    btn_read = document.getElementById("btn_read_" + id);
    btn_archive = document.getElementById("btn_archive_" + id);
    btn_favorite = document.getElementById("btn_favorite_" + id);

    btn_edit.style.display = "inline-block";
    btn_delete.style.display = "inline-block";
    btn_read.style.display = "inline-block";
    btn_archive.style.display = "inline-block";
    btn_favorite.style.display = "inline-block";
}


// On mouse out hide the buttons
function hide_buttons(id){
    // console.log("hide_buttons");
    btn_edit.style.display = 'none';
    btn_delete.style.display = 'none';
    btn_read.style.display = "none";
    btn_archive.style.display = "none";
    btn_favorite.style.display = "none";
}


function open_link(url){
    window.open(url, '_blank');
}


function handle_click(event){
    event.stopPropagation();
}


function change_view(view_option){
    const bookmarks = document.getElementsByClassName('list-group-item');
    let L = bookmarks.length;
    localStorage.setItem("view_option", view_option);

    for(let i = 0; i < L; i++){
        // const bookmark = bookmarks[i];
        // const img = bookmark.getElementsByTagName('img')[0];
        
        if(view_option === 'large'){
            // console.log('*large image');

            // Make button view active
            button_large_view = document.getElementById('dropdown_item_large');
            button_large_view.classList.add('active');
            button_small_view = document.getElementById('dropdown_item_small');
            button_small_view.classList.remove('active');

            /*
            // Show large images
            large_images = document.getElementsByClassName('bookmark_image_large');
            for(image of large_images){
                image.style.display = 'block';
            }

            // Hide small images
            small_images = document.getElementsByClassName('bookmark_image_small');
            for(image of small_images){
                image.style.display = 'none';
            }
            */

            // NEW CODE***
            // Show large images
            div_large_headings = document.getElementsByClassName('div_large_heading');
            for(heading of div_large_headings){
                heading.style.display = 'flex';
            }
            large_images = document.getElementsByClassName('bookmark_image_large');
            for(image of large_images){
                image.style.display = 'block';
            }

            // Hide small images
            div_small_headings = document.getElementsByClassName('div_small_heading');
            for(heading of div_small_headings){
                heading.style = 'display: none !important;';
            }
            
        }
        else if(view_option === 'small'){
            // console.log('*small image');

            // Make button view active
            button_large_view = document.getElementById('dropdown_item_large');
            button_large_view.classList.remove('active');
            button_small_view = document.getElementById('dropdown_item_small');
            button_small_view.classList.add('active');

            /*
            // Hide large images
            large_images = document.getElementsByClassName('bookmark_image_large');
            for(image of large_images){
                image.style.display = 'none';
            }

            // Show small images
            small_images = document.getElementsByClassName('bookmark_image_small');
            for(image of small_images){
                image.style.display = 'block';
            }
            */

            // NEW CODE***
            // Hide large images
            div_large_headings = document.getElementsByClassName('div_large_heading');
            for(heading of div_large_headings){
                heading.style = 'display: none !important;';
            }
            large_images = document.getElementsByClassName('bookmark_image_large');
            for(image of large_images){
                image.style.display = 'none';
            }

            // Show small images
            div_small_headings = document.getElementsByClassName('div_small_heading');
            for(heading of div_small_headings){
                heading.style.display = 'flex';
            }

        }
    }
}


const saved_view_option = localStorage.getItem("view_option");
if(saved_view_option){
    change_view(saved_view_option);
}

if(!saved_view_option){
    change_view('large');
}


function form_readed(bookmark_id){
    var form_readed = document.getElementById("form_readed_" + bookmark_id);
    form_readed.submit();
}
