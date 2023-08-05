//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var TextureModel = require('./Texture.autogen.js').TextureModel;


class CompressedTextureModel extends TextureModel {

    defaults() {
        return _.extend(TextureModel.prototype.defaults.call(this), {


        });
    }

    constructThreeObject() {

        var result = new THREE.CompressedTexture();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        TextureModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['id'] = true;
        this.props_created_by_three['version'] = true;



    }
}

CompressedTextureModel.model_name = 'CompressedTextureModel';
CompressedTextureModel.serializers = {
    ...TextureModel.serializers,
};

module.exports = {
    CompressedTextureModel: CompressedTextureModel,
};
