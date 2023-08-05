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


class RawShaderMaterialModel extends ShaderMaterialModel {

    defaults() {
        return _.extend(ShaderMaterialModel.prototype.defaults.call(this), {

            type: "RawShaderMaterial",

        });
    }

    constructThreeObject() {

        var result = new THREE.RawShaderMaterial(
            {
                type: this.get('type'),
            }
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ShaderMaterialModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['extensions'] = true;
        this.props_created_by_three['type'] = true;

        this.property_converters['type'] = null;


    }
}

RawShaderMaterialModel.model_name = 'RawShaderMaterialModel';
RawShaderMaterialModel.serializers = {
    ...ShaderMaterialModel.serializers,
};

module.exports = {
    RawShaderMaterialModel: RawShaderMaterialModel,
};
