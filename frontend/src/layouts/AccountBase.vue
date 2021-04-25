<template>
    <div class="accounts-base">
        <div class="accounts-form elevation">
            <slot></slot>

            <ErrorModal />
            <Loader />
        </div>
    </div>
</template>

<script>
    import '@/assets/css/accounts.css'
    import ErrorModal from '@/components/common/ErrorModal.vue'
    import Loader from '@/components/common/Loader.vue'

    export default {
        name: 'AccountBase',
        components: {
            ErrorModal,
            Loader
        }
    }
</script>
