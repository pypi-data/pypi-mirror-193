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


class SkeletonHelperModel extends Object3DModel {

    defaults() {
        return _.extend(Object3DModel.prototype.defaults.call(this), {

            root: null,
            type: "SkeletonHelper",

        });
    }

    constructThreeObject() {

        var result = new THREE.SkeletonHelper(
            this.convertThreeTypeModelToThree(this.get('root'), 'root')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        Object3DModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('root');

        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['root'] = 'convertThreeType';
        this.property_converters['type'] = null;


    }
}

SkeletonHelperModel.model_name = 'SkeletonHelperModel';
SkeletonHelperModel.serializers = {
    ...Object3DModel.serializers,
    root: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    SkeletonHelperModel: SkeletonHelperModel,
};
