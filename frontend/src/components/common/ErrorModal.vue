<template>
    <div class="modal" :style="{ display: get_display }">
        <div class="modal-content">
            <div class="modal-header form-header flex-h-center space-around">
                Something went wrong ...
                <button class="flex-1 btn-small danger bg-img-none fntz-9 pa-1" @click="close_modal">&times;</button>
            </div>

            <div class="modal-body">
                <p
                    v-for="(error, error_index) in get_error"
                    :key="error_index"
                >
                    <label class="text-center text-black form-header">
                        {{ error }}
                    </label>
                </p>

                <p
                    v-for="(success, success_index) in get_success"
                    :key="success_index"
                >
                    <label class="text-center text-black form-header">
                        {{ success }}
                    </label>
                </p>
            </div>
        </div>
    </div>
</template>

<script>
    import { mapGetters, mapMutations } from 'vuex'
    import * as types from '@/store/types.js'

    export default {
        name: 'ErrorModal',
        computed: {
            ...mapGetters({
                error: 'get_error',
                success: 'get_success'
            }),
            get_error () {
                var errors = []

                if (this.error != null) {
                    var keys = Object.keys(this.error)

                    for (var i = 0; i < keys.length; i++) {
                        var message = this.error[keys[i]]
                        errors.unshift(message)
                    }
                }

                return errors
            },
            get_success () {
                var successes = []

                if (this.success != null) {
                    var keys = Object.keys(this.success)

                    for (var i = 0; i < keys.length; i++) {
                        var message = this.success[keys[i]]
                        successes.unshift(message)
                    }
                }

                return successes
            },
            get_display () {
                if (this.error == null) {
                    return 'none'
                } else {
                    return 'block'
                }
            }
        },
        methods: {
            ...mapMutations({
                clear_error: types.CLEAR_ERROR,
                clear_success: types.CLEAR_SUCCESS
            }),
            close_modal () {
                this.clear_error()
                this.clear_success()
            }
        }
    }
</script>
