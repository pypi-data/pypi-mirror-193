//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var MeshPhongMaterialModel = require('./MeshPhongMaterial.autogen.js').MeshPhongMaterialModel;

var TextureModel = require('../textures/Texture.autogen.js').TextureModel;

class MeshToonMaterialModel extends MeshPhongMaterialModel {

    defaults() {
        return _.extend(MeshPhongMaterialModel.prototype.defaults.call(this), {

            gradientMap: null,
            type: "MeshToonMaterial",

        });
    }

    constructThreeObject() {

        var result = new THREE.MeshToonMaterial();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        MeshPhongMaterialModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('gradientMap');

        this.props_created_by_three['type'] = true;

        this.property_converters['gradientMap'] = 'convertThreeType';
        this.property_converters['type'] = null;


    }
}

MeshToonMaterialModel.model_name = 'MeshToonMaterialModel';
MeshToonMaterialModel.serializers = {
    ...MeshPhongMaterialModel.serializers,
    gradientMap: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    MeshToonMaterialModel: MeshToonMaterialModel,
};
