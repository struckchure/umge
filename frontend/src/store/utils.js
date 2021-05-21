export function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


export class Storage {

    get(key) {
        let get_value;
        try {
            var storage_value = localStorage.getItem(key)
            get_value = storage_value
        } catch {
            get_value = null
        }

        return get_value
    }

    set(key, value) {
        localStorage.setItem(key, value)
    }

    remove(key) {
        localStorage.removeItem(key)
    }
}


export function order_color (status) {
    var classes = [];

    // classes.unshift('rounded text-white')

    var PENDING_COLOR = 'bg-blue-600'
    var PROCESSING_COLOR = 'bg-green-600'
    var DONE_COLOR = 'bg-green-700'
    var CANCELLED_COLOR = 'bg-red-600'

    switch (status) {
        case 'PD':
            classes.unshift(PENDING_COLOR)
            break;
        case 'PS':
            classes.unshift(PROCESSING_COLOR)
            break;
        case 'DN':
            classes.unshift(DONE_COLOR)
            break;
        case 'CD':
            classes.unshift(CANCELLED_COLOR)
            break;
    }

    return classes
}

export function order_icon (status) {
    var classes = [];

    classes.unshift('fas')

    var PENDING_ICON = 'fa-stop'
    var PROCESSING_ICON = 'fa-spinner'
    var DONE_ICON = 'fa-check'
    var CANCELLED_ICON = 'fa-times-circle'

    switch (status) {
        case 'PD':
            classes.unshift(PENDING_ICON)
            break;
        case 'PS':
            classes.unshift(PROCESSING_ICON)
            break;
        case 'DN':
            classes.unshift(DONE_ICON)
            break;
        case 'CD':
            classes.unshift(CANCELLED_ICON)
            break;
    }

    return classes
}
