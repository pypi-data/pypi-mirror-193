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


class BoxHelperModel extends Object3DModel {

    defaults() {
        return _.extend(Object3DModel.prototype.defaults.call(this), {

            object: null,
            color: "#ffffff",
            type: "BoxHelper",

        });
    }

    constructThreeObject() {

        var result = new THREE.BoxHelper(
            this.convertThreeTypeModelToThree(this.get('object'), 'object'),
            this.convertColorModelToThree(this.get('color'), 'color')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        Object3DModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('object');

        this.props_created_by_three['matrixAutoUpdate'] = true;
        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['object'] = 'convertThreeType';
        this.property_converters['color'] = 'convertColor';
        this.property_converters['type'] = null;


    }
}

BoxHelperModel.model_name = 'BoxHelperModel';
BoxHelperModel.serializers = {
    ...Object3DModel.serializers,
    object: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    BoxHelperModel: BoxHelperModel,
};
