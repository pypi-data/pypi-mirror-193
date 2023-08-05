//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var Object3DModel = require('../core/Object3D.js').Object3DModel;

var SpriteMaterialModel = require('../materials/SpriteMaterial.autogen.js').SpriteMaterialModel;

class SpriteModel extends Object3DModel {

    defaults() {
        return _.extend(Object3DModel.prototype.defaults.call(this), {

            material: null,
            center: [0.5,0.5],
            type: "Sprite",

        });
    }

    constructThreeObject() {

        var result = new THREE.Sprite(
            this.convertThreeTypeModelToThree(this.get('material'), 'material')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        Object3DModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('material');

        this.props_created_by_three['skeleton'] = true;
        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['material'] = 'convertThreeType';
        this.property_converters['center'] = 'convertVector';
        this.property_converters['type'] = null;

        this.property_assigners['center'] = 'assignVector';

    }
}

SpriteModel.model_name = 'SpriteModel';
SpriteModel.serializers = {
    ...Object3DModel.serializers,
    material: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    SpriteModel: SpriteModel,
};
