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


class Box3Model extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            min: [0,0,0],
            max: [0,0,0],

        });
    }

    constructThreeObject() {

        var result = new THREE.Box3(
            this.convertVectorModelToThree(this.get('min'), 'min'),
            this.convertVectorModelToThree(this.get('max'), 'max')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);


        this.property_converters['min'] = 'convertVector';
        this.property_converters['max'] = 'convertVector';

        this.property_assigners['min'] = 'assignVector';
        this.property_assigners['max'] = 'assignVector';

    }
}

Box3Model.model_name = 'Box3Model';
Box3Model.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    Box3Model: Box3Model,
};
