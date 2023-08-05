//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../../_base/serializers');

var ThreeModel = require('../../_base/Three.js').ThreeModel;


class DiscreteInterpolantModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {


        });
    }

    constructThreeObject() {

        var result = new THREE.DiscreteInterpolant();
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);




    }
}

DiscreteInterpolantModel.model_name = 'DiscreteInterpolantModel';
DiscreteInterpolantModel.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    DiscreteInterpolantModel: DiscreteInterpolantModel,
};
