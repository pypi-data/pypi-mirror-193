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


class CubeTextureModel extends TextureModel {

    defaults() {
        return _.extend(TextureModel.prototype.defaults.call(this), {

            images: [],

        });
    }

    constructThreeObject() {

        var result = new THREE.CubeTexture(
            this.get('images'),
            this.convertEnumModelToThree(this.get('mapping'), 'mapping'),
            this.convertEnumModelToThree(this.get('wrapS'), 'wrapS'),
            this.convertEnumModelToThree(this.get('wrapT'), 'wrapT'),
            this.convertEnumModelToThree(this.get('magFilter'), 'magFilter'),
            this.convertEnumModelToThree(this.get('minFilter'), 'minFilter'),
            this.convertEnumModelToThree(this.get('format'), 'format'),
            this.convertEnumModelToThree(this.get('type'), 'type'),
            this.convertFloatModelToThree(this.get('anisotropy'), 'anisotropy')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        TextureModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['id'] = true;
        this.props_created_by_three['version'] = true;

        this.property_converters['images'] = null;

        this.property_assigners['images'] = 'assignArray';

    }
}

CubeTextureModel.model_name = 'CubeTextureModel';
CubeTextureModel.serializers = {
    ...TextureModel.serializers,
};

module.exports = {
    CubeTextureModel: CubeTextureModel,
};
