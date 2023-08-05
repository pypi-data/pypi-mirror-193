//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var ThreeModel = require('../_base/Three.js').ThreeModel;


class CompressedTextureLoaderModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {


        });
    }

    constructThreeObject() {

        var result = new THREE.CompressedTextureLoader();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);




    }
}

CompressedTextureLoaderModel.model_name = 'CompressedTextureLoaderModel';
CompressedTextureLoaderModel.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    CompressedTextureLoaderModel: CompressedTextureLoaderModel,
};
