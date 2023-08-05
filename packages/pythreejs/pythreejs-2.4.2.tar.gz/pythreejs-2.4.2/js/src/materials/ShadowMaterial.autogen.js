//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var ShaderMaterialModel = require('./ShaderMaterial.autogen.js').ShaderMaterialModel;


class ShadowMaterialModel extends ShaderMaterialModel {

    defaults() {
        return _.extend(ShaderMaterialModel.prototype.defaults.call(this), {

            lights: true,
            transparent: true,
            type: "ShadowMaterial",

        });
    }

    constructThreeObject() {

        var result = new THREE.ShadowMaterial();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ShaderMaterialModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['extensions'] = true;
        this.props_created_by_three['type'] = true;

        this.property_converters['lights'] = 'convertBool';
        this.property_converters['transparent'] = 'convertBool';
        this.property_converters['type'] = null;


    }
}

ShadowMaterialModel.model_name = 'ShadowMaterialModel';
ShadowMaterialModel.serializers = {
    ...ShaderMaterialModel.serializers,
};

module.exports = {
    ShadowMaterialModel: ShadowMaterialModel,
};
