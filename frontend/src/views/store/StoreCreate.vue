<template>
    <Base current_page="Profile" page_title="Profile">
        <template v-slot:main>
            <div class="row">
                <div class="col s12 m4 m4">
                    <UserPreview />
                </div>

                <div class="col s12 m8 m8">
                    <div class="user-update">
                        <label class="form-header">Store / <span style="color: #333;">New</span></label>
                        <form @submit.prevent="save_store" enctype="multipart/form-data">
                            <div class="row">
                                <div class="col s12 m12 l12">
                                    <label class="form-label text-left">Store name</label>
                                </div>

                                <div class="col s12 m12 l12">
                                    <input
                                        type="text"
                                        placeholder="Store name"
                                        maxlength="20"
                                        v-model="store_name"
                                    />
                                </div>

                                <div class="col s12 m12 l12">
                                    <label class="form-label text-left">Store image</label>
                                </div>

                                <div class="col s12 m12 l12">
                                    <input type="file" ref="store_image" @change="handleImageUpload" />
                                </div>

                                <div class="col s12 m12 l12">
                                    <label class="form-label text-left">Store description</label>
                                </div>

                                <div class="col s12 m12 l12">
                                    <textarea
                                        placeholder="store description"
                                        v-model="store_description"
                                    ></textarea>
                                </div>

                                <div class="col s12 m12 l12">
                                    <label class="form-label text-left">
                                        Store package
                                    </label>
                                </div>

                                <div class="col s12 m12 l12">
                                    <select v-model="store_package">
                                        <option value="BSC">Basic plan</option>
                                        <option value="STD">Standard plan</option>
                                        <option value="PRM">Premium plan</option>
                                    </select>
                                </div>

                                <div class="col s12 m12 l12">
                                    <label class="form-label text-left">Store E-Mail</label>
                                </div>

                                <div class="col s12 m12 l12">
                                    <input
                                        type="email"
                                        placeholder="store e-mail"
                                        maxlength="40"
                                        v-model="store_email"
                                    />
                                </div>

                                <div class="col s12 m12 l12">
                                    <label class="form-label text-left">Store phone number</label>
                                </div>

                                <div class="col s3 m2 l2">
                                    <input
                                        type="number"
                                        placeholder="store phone number"
                                        v-model="country_code"
                                        readonly
                                    />
                                </div>

                                <div class="col s9 m10 l10">
                                    <input
                                        type="number"
                                        placeholder="store phone number"
                                        maxlength="15"
                                        v-model="store_phone_number"
                                    />
                                </div>
                            </div>

                            <button type="submit">Save store</button>
                        </form>
                    </div>
                </div>
            </div>
        </template>
    </Base>
</template>

<script>
    import UserPreview from '@/components/accounts/UserPreview.vue'

    import { mapGetters, mapActions } from 'vuex'
    import * as types from '@/store/types.js'

    export default {
        name: 'StoreCreate',
        title () {
            return 'Store | Create'
        },
        data () {
            return {
                store_name: '',
                store_image: '',
                store_description: '',
                store_email: '',
                store_package: '',
                store_phone_number: '',
                country_code: '+234'
            }
        },
        computed: {
            ...mapGetters({
                user: 'get_user',
                store: 'get_store'
            }),
            get_full_name () {
                if (this.user.username) {
                    if (this.user.first_name.length > 0 && this.user.last_name.length > 0) {
                        return `${this.user.first_name} ${this.user.last_name}`
                    } else {
                        return this.user.username
                    }
                } else {
                    return 'loading ...'
                }
            }
        },
        components: {
            UserPreview
        },
        methods: {
            ...mapActions({
                'create_store': types.CREATE_STORE
            }),
            handleImageUpload (event) {
                this.store_image = event.target.files[0]
            },
            save_store () {
                const payload = {
                    store_name: this.store_name,
                    store_image: this.store_image,
                    store_description: this.store_description,
                    store_email: this.store_email,
                    store_package: this.store_package,
                    store_phone_number: this.store_phone_number,
                    store_owner: this.user.id
                }

                this.create_store(payload)
            }
        }
    }
</script>
