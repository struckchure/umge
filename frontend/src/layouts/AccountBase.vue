<template>
    <div class="accounts-base h-screen">
        <div class="accounts-form elevation">
            <slot></slot>

            <ErrorModal />
            <Loader />
        </div>
    </div>
</template>

<style scoped>
    .input-field {
        width: 100%;
    }

    input {
        width: inherit;
    }

    button.social {
        width: 40px;
        height: 40px;
    }

    i {
        display: flex;
        align-items: center;
    }

    input, i {
        height: 50px !important;
    }

    .form-title {
        font-size: 1.5em;
    }
</style>

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
