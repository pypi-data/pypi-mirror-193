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


class CylindricalModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            radius: 1,
            theta: 0,
            y: 0,

        });
    }

    constructThreeObject() {

        var result = new THREE.Cylindrical(
            this.convertFloatModelToThree(this.get('radius'), 'radius'),
            this.convertFloatModelToThree(this.get('theta'), 'theta'),
            this.convertFloatModelToThree(this.get('y'), 'y')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);


        this.property_converters['radius'] = 'convertFloat';
        this.property_converters['theta'] = 'convertFloat';
        this.property_converters['y'] = 'convertFloat';


    }
}

CylindricalModel.model_name = 'CylindricalModel';
CylindricalModel.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    CylindricalModel: CylindricalModel,
};
