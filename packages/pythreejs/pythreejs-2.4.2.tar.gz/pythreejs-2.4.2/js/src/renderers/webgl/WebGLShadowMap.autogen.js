//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../../_base/serializers');

var ThreeModel = require('../../_base/Three.js').ThreeModel;


class WebGLShadowMapModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            enabled: false,
            type: "PCFShadowMap",

        });
    }

    constructThreeObject() {

        var result = new THREE.WebGLShadowMap();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);

        this.enum_property_types['type'] = 'ShadowTypes';

        this.property_converters['enabled'] = 'convertBool';
        this.property_converters['type'] = 'convertEnum';


    }
}

WebGLShadowMapModel.model_name = 'WebGLShadowMapModel';
WebGLShadowMapModel.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    WebGLShadowMapModel: WebGLShadowMapModel,
};
