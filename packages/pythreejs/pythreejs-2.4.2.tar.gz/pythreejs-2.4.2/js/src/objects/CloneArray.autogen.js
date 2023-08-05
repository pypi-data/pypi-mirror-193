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


class CloneArrayModel extends Object3DModel {

    defaults() {
        return _.extend(Object3DModel.prototype.defaults.call(this), {

            original: null,
            positions: [],
            merge: false,
            type: "CloneArray",

        });
    }

    constructThreeObject() {

        var result = new THREE.CloneArray(
            this.convertThreeTypeModelToThree(this.get('original'), 'original'),
            this.convertVectorArrayModelToThree(this.get('positions'), 'positions'),
            this.convertBoolModelToThree(this.get('merge'), 'merge')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        Object3DModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('original');

        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['original'] = 'convertThreeType';
        this.property_converters['positions'] = 'convertVectorArray';
        this.property_converters['merge'] = 'convertBool';
        this.property_converters['type'] = null;

        this.property_assigners['positions'] = 'assignArray';

    }
}

CloneArrayModel.model_name = 'CloneArrayModel';
CloneArrayModel.serializers = {
    ...Object3DModel.serializers,
    original: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    CloneArrayModel: CloneArrayModel,
};
