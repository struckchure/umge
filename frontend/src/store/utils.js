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
        try {
            var storage_value = localStorage.getItem(key)
            if (storage_value) {
                get_value = JSON.parse(storage_value)
            }
        } catch {
            var get_value = null
        }

        return get_value
    }

    set(key, value) {
        var set_value = JSON.stringify(value)

        localStorage.setItem(key, set_value)
    }

    remove(key) {
        localStorage.removeItem(key)
    }
}
