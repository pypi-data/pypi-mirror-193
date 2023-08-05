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

var PointLightModel = require('../lights/PointLight.autogen.js').PointLightModel;

class PointLightHelperModel extends Object3DModel {

    defaults() {
        return _.extend(Object3DModel.prototype.defaults.call(this), {

            light: null,
            sphereSize: 1,
            color: "#ffffff",
            type: "PointLightHelper",

        });
    }

    constructThreeObject() {

        var result = new THREE.PointLightHelper(
            this.convertThreeTypeModelToThree(this.get('light'), 'light'),
            this.convertFloatModelToThree(this.get('sphereSize'), 'sphereSize'),
            this.convertColorModelToThree(this.get('color'), 'color')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        Object3DModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('light');

        this.props_created_by_three['matrixAutoUpdate'] = true;
        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['light'] = 'convertThreeType';
        this.property_converters['sphereSize'] = 'convertFloat';
        this.property_converters['color'] = 'convertColor';
        this.property_converters['type'] = null;


    }
}

PointLightHelperModel.model_name = 'PointLightHelperModel';
PointLightHelperModel.serializers = {
    ...Object3DModel.serializers,
    light: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    PointLightHelperModel: PointLightHelperModel,
};
