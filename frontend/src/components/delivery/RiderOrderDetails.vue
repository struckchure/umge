<template>
    <div class="modal" :style="{ display: get_display }">
        <div class="modal-tools">
            <button @click="close_modal" class="modal-close">&times;</button>
        </div>

        <div class="modal-content">
            <div class="modal-header form-header px-8 flex items-center">
                Order / Details
            </div>

            <div class="modal-body">
                <p>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
                    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
                    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
                    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                </p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'RiderOrderDetails',
        props: [
            'order'
        ],
        data () {
            return {
                props_order: this.order
            }
        },
        mounted () {
            console.log(this.props_order)
        },
        computed: {
            get_display () {
                let display;

                if (this.props_order.user) {
                    display = 'block'
                } else {
                    display = 'none'
                }

                return display
            }
        },
        methods: {
            close_modal () {
                this.props_order = {}
            }
        }
    }
</script>
