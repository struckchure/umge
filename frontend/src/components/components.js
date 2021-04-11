import Vue from 'vue'

import Base from '@/layouts/Base.vue';

// components declarations

const components = {
	Base
}

Object.entries(components).forEach(([name, component]) => Vue.component(name, component))
