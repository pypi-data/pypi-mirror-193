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


class QuaternionModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            x: 0,
            y: 0,
            z: 0,
            w: 1,

        });
    }

    constructThreeObject() {

        var result = new THREE.Quaternion(
            this.convertFloatModelToThree(this.get('x'), 'x'),
            this.convertFloatModelToThree(this.get('y'), 'y'),
            this.convertFloatModelToThree(this.get('z'), 'z'),
            this.convertFloatModelToThree(this.get('w'), 'w')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);


        this.property_converters['x'] = 'convertFloat';
        this.property_converters['y'] = 'convertFloat';
        this.property_converters['z'] = 'convertFloat';
        this.property_converters['w'] = 'convertFloat';


    }
}

QuaternionModel.model_name = 'QuaternionModel';
QuaternionModel.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    QuaternionModel: QuaternionModel,
};
